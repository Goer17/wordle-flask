document.addEventListener('DOMContentLoaded', () => {
    let pop_up_short_info = document.querySelector('.pop-up-short-info');
    if (pop_up_short_info != null) {
        pop_up_short_info.style.display = 'block';

        setTimeout(() => {
            pop_up_short_info.style.display = 'none';
        }, 2000);
    }

    let close_button = document.querySelector('.pop-up-wind .close');
    if (close_button != null) {
        close_button.addEventListener('click', () => {
            close_button.closest('.pop-up-wind').style.display = 'none';
        });
    }
});