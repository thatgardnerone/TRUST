<script setup>
import { ref } from "vue";

import H2 from "@/Atoms/H2.vue";
import H3 from "@/Atoms/H3.vue";
import Input from "@/Atoms/Input.vue";
import Label from "@/Atoms/Label.vue";

defineProps({
    title: {
        type: String,
        default: "",
    },
    subtitle: {
        type: String,
        default: "",
    },
    description: {
        type: String,
        default: "",
    },
    dimensions: {
        type: Number,
        required: true,
    },
});

const vectorData = defineModel({ default: [] });
const inputError = ref(false);

const updateMatrix = (i, event) => {
    inputError.value = false;

    const oldValue = event.target.value;

    if (!oldValue) {
        vectorData.value[i - 1] = [];
        return;
    }

    const parsed = oldValue
        .split(",")
        .map(Number)
        .filter((value) => value !== undefined);

    inputError.value = parsed.some((value) => isNaN(value));
    inputError.value = parsed.length > 2;

    vectorData.value[i - 1] = parsed;
};
</script>

<template>
    <div class="py-1">
        <H2 v-if="title">{{ title }}</H2>
        <H3 v-else>{{ subtitle }}</H3>

        <p class="text-sm text-gray-400">
            {{ description }}
        </p>
        <div
            v-for="i in dimensions"
            :key="i"
            class="mt-2 flex rounded-md shadow-sm">
            <Label :for="`x${i}`">
                x<sub class="mt-1">{{ i }}</sub>
            </Label>
            <Input
                :id="`x${i}`"
                :has-error="inputError"
                :placeholder="i === 1 ? 'e.g. 1, 2' : '...'"
                aria-autocomplete="none"
                autocapitalize="off"
                autocomplete="off"
                required
                type="text"
                @input="updateMatrix(i, $event)" />
        </div>
    </div>
</template>

<style scoped></style>
