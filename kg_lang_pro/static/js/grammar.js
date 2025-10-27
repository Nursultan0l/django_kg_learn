function openGrammar(button) {
    const block = button.closest('.lesson-block');
    const description = block.nextElementSibling;
    description.classList.remove('hidden');
    button.classList.add('hidden');
    block.querySelector('.close-btn').classList.remove('hidden');
}

function closeGrammar(button) {
    const block = button.closest('.lesson-block');
    const description = block.nextElementSibling;
    description.classList.add('hidden');
    button.classList.add('hidden');
    block.querySelector('.open-btn').classList.remove('hidden');
}
