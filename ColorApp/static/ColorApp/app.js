function toggleDropdown(colorId) {
    const optionsList = document.getElementById(`${colorId}-options`);
    optionsList.style.display = optionsList.style.display === 'none' ? 'block' : 'none';
}

function selectColor(colorId, hexCode, colorName) {
    const colorBox = document.getElementById(`${colorId}-box`);
    const colorLabel = document.getElementById(`${colorId}-label`);
    const colorSelect = document.getElementById(`${colorId}-input`);

    colorBox.style.backgroundColor = hexCode;
    colorLabel.textContent = colorName;
    colorSelect.value = hexCode;

    toggleDropdown(colorId);
}
function copyToClipboard(color) {
    var dummy = document.createElement("textarea");
    document.body.appendChild(dummy);
    dummy.value = color;
    dummy.select();
    document.execCommand("copy");
    document.body.removeChild(dummy);
 }
function handleHexButtonClick(hexColor) {
    copyToClipboard(hexColor);
}
function handleColorBlockClick(hexColor) {
    copyToClipboard(hexColor);
}
 