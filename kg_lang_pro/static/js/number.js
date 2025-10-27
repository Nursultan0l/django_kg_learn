document.addEventListener('DOMContentLoaded', () => {
  const buttons2 = document.querySelectorAll('.voice_number');

  buttons2.forEach(button => {
    const audio = button.nextElementSibling; // <audio> идёт сразу после кнопки
    const icon = button.querySelector('ion-icon');

    button.addEventListener('click', () => {
      // Остановить все аудио, если одно уже играет
      document.querySelectorAll('audio').forEach(a => {
        if (!a.paused) {
          a.pause();
          a.currentTime = 0;
        }
      });

      // Сбросить все иконки
      document.querySelectorAll('.voice_letter ion-icon').forEach(i => {
        i.setAttribute('name', 'caret-forward');
      });

      // Проиграть текущее аудио
      if (audio.paused) {
        audio.play();
        icon.setAttribute('name', 'pause-circle');
      } else {
        audio.pause();
        icon.setAttribute('name', 'caret-forward');
      }
    });

    audio.addEventListener('ended', () => {
      icon.setAttribute('name', 'caret-forward');
    });
  });
});
