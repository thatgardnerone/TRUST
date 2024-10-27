import tracemalloc
from time import time
from typing import Union

from flask import Blueprint, Response, jsonify, request
from flask_inertia import lazy_include, render_inertia
import sympy as sp
from picos import SolutionFailure

import tests
from app.models.safety_barrier import SafetyBarrier
from app.models.stability import Stability

bp = Blueprint("dashboard", __name__)


def calculate_result() -> dict:
    """
    Calculate the result of the user's input.

    :return: the result of the calculation
    """

    # TODO: validate data
    data = request.get_json()

    tracemalloc.start()

    start_time = time()

    try:
        if data["mode"] == "Stability":
            results = Stability().create(data).calculate()
        else:
            results = SafetyBarrier(data).calculate()
    except SolutionFailure as e:
        results = {
            "error": "Solution Failure",
            "description": str(e),
        }
    except Exception as e:
        results = {
            "error": "An unknown error occurred.",
            "description": str(e),
        }

    time_taken = time() - start_time

    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    results["time_taken"] = f"{time_taken:.5f}s"
    results["memory_used"] = f"{peak / 10**6:.1f}MB"

    return results


def validate_monomials() -> bool | list:
    """
    Validate the user's input monomials.
    Monomials should be a list of strings separated by a semicolon, e.g. x1; 2 * x2; x3 - x1
    Each monomial term should be a valid mathematical expression, e.g. 2 * x2
    Each term should also only represent a valid dimension, e.g. x1 to xn, where n is the dimension
    of the dataset.

    :return: Whether the monomials are valid
    """

    monomials = request.get_json()["monomials"]
    if not monomials["terms"]:
        return False

    # Use sympy to validate the monomials
    terms = []
    for monomial in monomials["terms"]:
        print(monomial)
        try:
            terms.append(sp.sympify(monomial))
        except sp.SympifyError:
            return False

    # Get the x terms, and check if they are in the correct format
    # i.e. x1 to xn, where n is the number of dimensions
    # e.g. x1**2; x2 + 2 is valid if dimensions = 2
    dimensions = monomials["dimensions"]
    for term in terms:
        for x in term.atoms(sp.Symbol):
            if (
                not x.name.startswith("x")
                or not x.name[1:].isdigit()
                or int(x.name[1:]) > dimensions
            ):
                return False

    return monomials


@bp.route("/", endpoint="index", methods=["GET", "POST"])
def index():
    # TODO: use enums for easier refactoring
    models = [
        {"title": "Linear", "description": ""},
        {"title": "Non-Linear Polynomial", "description": ""},
    ]

    timings = [
        {"title": "Discrete-Time", "description": ""},
        {"title": "Continuous-Time", "description": ""},
    ]

    modes = [
        {"title": "Stability", "description": ""},
        {"title": "Safety", "description": ""},
        {"title": "Reachability", "description": "", "disabled": True},
        {"title": "Reach and Avoid", "description": "", "disabled": True},
    ]

    return render_inertia(
        "Dashboard",
        {
            "models": models,
            "timings": timings,
            "modes": modes,
            "monomials": lazy_include(validate_monomials),
            "result": lazy_include(calculate_result),
        },
    )
