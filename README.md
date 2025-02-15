# TRUST

[//]: # ([![DOI]&#40;https://zenodo.org/badge/788965518.svg&#41;]&#40;https://zenodo.org/doi/10.5281/zenodo.11085376&#41;[![CC BY 4.0][cc-by-shield]][cc-by])

<p align="center">
<img src="storage/images/TRUST.png" alt="" width="800"/>
</p>

**TRUST** is an  open-source software tool developed for data-driven controller synthesis of dynamical systems with unknown mathematical models, ensuring either stability or safety properties. By collecting only a single input-state trajectory from the unknown system and satisfying a rank condition that ensures the system is persistently excited according to Willems *et al.*'s fundamental lemma, **TRUST** aims to design either control Lyapunov functions (CLF) or control barrier certificates (CBC), along with their corresponding stability or safety controllers. The tool implements sum-of-squares (SOS) optimization programs solely based on data to enforce stability or safety properties across four system classes:
- _continuous-time nonlinear polynomial systems_,
- _continuous-time linear systems_,
- _discrete-time nonlinear polynomial systems_, and
- _discrete-time linear systems_.

**TRUST** is a Python-based web application featuring an intuitive, reactive graphic user interface (GUI) built with web technologies. It can be accessed at <https://trust.tgo.dev> or installed locally, and supports both manual data entry and data file uploads. Leveraging the power of the Python backend and a JavaScript frontend, **TRUST** is designed to be highly user-friendly and accessible across desktop, laptop, tablet, and mobile devices. We apply **TRUST** to a set of physical benchmarks with unknown dynamics, ensuring either stability or safety properties across the four supported classes of models.

## Table of Contents
- [Artifact Evaluation](#Artifact-Evaluation)
- [Installation](#install-instructions)
- [Examples](#examples)
- [Error Handling](#error-handling)
- [Related Paper](#related-paper)
- [Contributing Guide](#contributing-guide)
- [License](#license)

## Artifact Evaluation

> If you are a reviewer for the HSCC committee, the instructions for how to install and reproduce the results of our paper can be found [here](./TRUST__repeatability_instructions.pdf). 

We recommend running the tool via Docker, instructions in the installation section following.

A hosted version of the tool is available at <https://trust.tgo.dev> for you to explore the tool's capabilities, but note that the capacity of the server is limited and is unlikely to perform as well as a local installation.

# Install Instructions

We have made every effort to ensure the following instructions are comprehensive for the Docker container under consideration.

## Prerequisites

### Docker
Docker is used for this project to simplify the installation process. You can download and install Docker by following their instructions for your operating system at <https://docs.docker.com/get-docker/>.

### Mosek License
Since the underlying packages that TRUST uses rely on the MOSEK solver, we will now install the MOSEK license (a free trial is available and it is free for academic users). Fill in your details to get a Mosek license at <https://www.mosek.com/license/request/?i=acp>.

The license file will be emailed to you with instructions of where to place the file in your home directory. This license is required within the TRUST GUI, where you will be prompted to upload the file.

## Installing TRUST

You can download the repository from Github at <https://github.com/thatgardnerone/TRUST>. Simply navigate to the page and click the green "Code" button, then "Download ZIP". Once downloaded, unzip the folder to your home directory which on Windows is usually `C:\Users\YourUsername` and on macOS and Linux is `/home/YourUsername`.

Change the folder name to `TRUST` to simplify the later steps.

The following steps will be run in a terminal. You can open a terminal on macOS by pressing `Cmd + Space` and typing "Terminal", or on Windows by pressing `Win + R` and typing `cmd`, then pressing `Enter`. On Linux, search for it in the applications menu as it varies by distribution.


### Change directory to TRUST
Once you have a terminal open, navigate to the `TRUST` folder by running the following

```bash
# On macOS and Linux
cd ~/TRUST
```
Or on Windows
```cmd
cd $HOME\TRUST
```

### Copy the environment file
The project contains an example environment file `.env.example`, containing environment configuration variables that you may change, if needed.
You can copy the example to a new file called `.env` by running:
    
```bash
# On macOS and Linux
cp .env.example .env
```
Or on Windows
```cmd
copy .env.example .env
```

### Build and run the Docker container
Next, build and run the Docker container by running:

```bash
# On any OS
docker compose up --build -d
```

### View the tool
Finally, you can now access the locally installed tool by navigating to `http://127.0.0.1:5000` in your web browser.

# Examples

We present some selected examples graphically to demonstrate some use cases of TRUST. 
All the examples can be found in the folder `TRUST/storage/cases` where the case studies are organised in subfolders each containing the necessary data files and inputs for the example.

For each of the safety examples, the following conventions are used.
- The initial region is shown in blue.
- The unsafe region(s) are shown in red.
- The gamma level set is shown in dashed red lines.
- The lambda level set is shown in dashed blue lines.
- Trajectories are shown in black, starting from the initial region and staying within the safe level set.

> Note: These figures were rendered using a MATLAB script that is not included in the repository. Please feel free to reach out if you would like to know more about how these figures were generated.

### Examples 1 and 2 - Continuous Time Nonlinear Polynomial Systems (Safety)
<p align="center">
    <img src="./storage/images/ctNPS_predator_prey_new.png" width="400"/>
    <img src="./storage/images/ctNPS_van_der_pol_oscillator.png" width="400"/>
</p>

First figure: ct-NPS predator-prey system

Second figure: ct-NPS Van der Pol oscillator system

### Example 3 to 5 - Continuous Time Linear Systems (Safety)
<p align="center">
<img src="./storage/images/ctLS_dc_motor.png" width="400"/>
<img src="./storage/images/ctLS_room_temp.png" width="400"/>
<img src="./storage/images/ctLS_two_tank.png" width="400"/>
</p>

First figure: ct-LS DC motor system

Second figure: ct-LS room temperature system

Third figure: ct-LS two-tank system

### Examples 6 and 7 - Discrete Time Nonlinear Polynomial Systems (Safety)
<p align="center">
<img src="./storage/images/dtNPS_predator_prey.png" width="400"/>
<img src="./storage/images/dtNPS_lorenz_smalltau.png" width="400"/>
</p>

First figure: dt-NPS predator-prey system

Second figure: dt-NPS Lorenz system

### Examples 8 to 11 - Discrete Time Linear Systems (Safety)

<p align="center">
<img src="./storage/images/dtLS_dc_motor.png" width="400"/>
<img src="./storage/images/dtLS_room_temp.png" width="400"/>
<img src="./storage/images/dtLS_3D_room_temp.png" width="400"/>
<img src="./storage/images/dtLS_two_tank.png" width="400"/>
</p>

First figure: dt-LS DC motor system

Second figure: dt-LS room temperature system

Third figure: 3D dt-LS room temperature system

Fourth figure: dt-LS two-tank system

### Examples 12 and 13 - Continuous Time Nonlinear Polynomial Systems (Stability)

<p align="center">
<img src="./storage/images/stability_ctNPS_predator_prey.png" width="400"/>
<img src="./storage/images/stability_ctNPS_van_der_pol_oscillator.png" width="400"/>

First figure: ct-NPS predator-prey system

Second figure: ct-NPS Van der Pol oscillator system

### Examples 14 to 16 - Continuous Time Linear Systems (Stability)

<p align="center">
<img src="./storage/images/stability_ctLS_dc_motor.png" width="400"/>
<img src="./storage/images/stability_ctLS_room_temp.png" width="400"/>
<img src="./storage/images/stability_ctLS_two_tank.png" width="400"/>

First figure: ct-LS DC motor system

Second figure: ct-LS room temperature system

Third figure: ct-LS two-tank system

### Examples 17 and 18 - Discrete Time Nonlinear Polynomial Systems (Stability)

<p align="center">
<img src="./storage/images/stability_dtNPS_academic.png" width="400"/>
<img src="./storage/images/stability_Lorenz_dtNPS.png" width="400"/>

First figure: dt-NPS academic system

Second figure: dt-NPS Lorenz system

### Examples 19 to 22 - Discrete Time Linear Systems (Stability)

<p align="center">
<img src="./storage/images/stability_dtLS_dc_motor.png" width="400"/>
<img src="./storage/images/stability_dtLS_room_temp.png" width="400"/>
<img src="./storage/images/stability_dtLS_3D_room_temp.png" width="400"/>
<img src="./storage/images/stability_dtLS_two_tank.png" width="400"/>

First figure: dt-LS DC motor system

Second figure: dt-LS room temperature system

Third figure: 3D dt-LS room tem§perature system

Fourth figure: dt-LS two-tank system

## Error Handling

TRUST is developed as a responsive and reactive Python Flask web application, offering an **intuitive, user-friendly** interface that allows seamless interaction. If a user error occurs, TRUST provides responsive error messages to guide the user in correcting their input. Listed below are some common errors that may be returned to the user:

1. For an invalid "state space", "initial set" or "unsafe set(s)": **"Provided spaces are not valid. Please provide valid lower and upper bounds."**
2. For an invalid shape of \(\Theta(x)\): **"Theta\_x should be of shape ({N}, {n})".**
3. If monomials are provided with commas: **"Monomial terms should be split by semicolon"**; if they are not suitable for the set dimensions: **"Monomials must be in terms of x1 (to xn)"**; if some unspecified error has occurred with the monomials: **"Invalid monomial terms."**
4. If the rank condition is not met for nonlinear polynomial systems: **"The number of samples, T, must be greater than the number of monomial terms, N"**, or **"The N0 data is not full row-rank"** depending on which part of the rank condition failed. Similarly for linear systems: **"The number of samples, T, must be greater than the number of states, n"**, or **"The X0 data is not full row-rank"** again depending on which part of the rank condition failed.
5. If data files are uploaded with an invalid format: **"Unable to parse uploaded file(s)".**
6. If the MOSEK solver cannot find a solution for the given values: **"Solution Failure,"** with a dynamic error description provided by the solver. If the MOSEK solver did find a solution but the solution does not contain an SOS decomposition: **"No SOS decomposition found,"** with a dynamic error description. Similarly, if the solution does not contain valid SOS constraints: **"Constraints are not sum-of-squares."**
7. Any other errors in the tool will be caught with the generic error message: **"An unknown error occurred,"** and a brief description that can be reported.

## Related Paper

The arXiv version of the paper is located [here]().

### Authors
- [Jamie Gardner](https://github.com/thatgardnerone)
- [Ben Wooding](https://woodingben.com)
- [Amy Nejati](https://www.amy-nejati.de/)
- [Abolfazl Lavaei](https://lavaei-cps.de/)

### Citing TRUST

```
@misc{TRUST2025,
      title={TRUST: StabiliTy and Safety ContRoller Synthesis for Unknown Dynamical Models Using a Single Trajectory}, 
      author={Jamie Gardne, Ben Wooding, Amy Nejati, and Abolfazl Lavaei},
      year={2025},
      eprint={tbc},
      journal={28th ACM International Conference on Hybrid Systems: Computation and Control (HSCC 2025)},
      primaryClass={eess.SY}
}
```

## Contributing Guide
If you encounter any issues or have feedback, please open an issue in the repository or submit a pull request. We appreciate your input and will address it as soon as possible.

## License
This work is licensed under a
[Creative Commons Attribution 4.0 International License][cc-by].

[![CC BY 4.0][cc-by-image]][cc-by]

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg
