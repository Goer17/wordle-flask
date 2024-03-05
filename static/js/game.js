let cells = document.getElementsByClassName('wordle-cell');

if (5 * focus < cells.length) {
    cells[5 * focus].focus()
}

for (let i = 0; i < cells.length; i++) {
    cells[i].addEventListener('input', e => {
        let value = e.target.value;
        let match = value.match(/[a-zA-Z]/);
        if (match && match[0]) {
            value = match[0].toUpperCase();
            if (i < cells.length - 1) {
                cells[i + 1].focus();
            }
        } else {
            e.target.value = ''
        }
    });

    cells[i].addEventListener('keydown', e => {
        if (e.key === 'Backspace') {
            e.preventDefault()
            cells[i].value = ''
            if (i > 0) {
                cells[i - 1].focus();
            }
        }
    });
}

let form = document.getElementById('wordle-block');
form.addEventListener('keypress', e => {
    if (e.key == 'Enter') {
        e.preventDefault()
        form.submit()
    }
})