function textfieldOnFocusHandler(source_input_element) {
    if (source_input_element.value == source_input_element.defaultValue) {
        source_input_element.value = ""
    }
}

function textfieldOnBlurHandler(source_input_element) {
    if (!source_input_element.value) {
        source_input_element.value = source_input_element.defaultValue
    }
}
