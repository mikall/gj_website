/*
 * document.addEventListener('DOMContentLoaded', function () {
    const words = ["it's easy", "it's cozy", "it's cool"];
    let i = 0;
    const autotypeElements = document.querySelectorAll('.autotype-variation');

    function changeWord() {
        autotypeElements.forEach(element => {
            element.classList.add('fade-out');
        });

        setTimeout(() => {
            autotypeElements.forEach(element => {
                element.textContent = words[i];
                element.classList.remove('fade-out');
            });
            i = (i + 1) % words.length;
        }, 500); // This value should match the CSS transition duration
    }

    setInterval(changeWord, 2000); // Change the word every 2 seconds
});
*/

document.addEventListener('DOMContentLoaded', function () {
    var typed = new Typed(document.getElementById('autotype-variation'), {
		strings: ['easy^1000', 'cozy^1000', 'cool^1000'],
		typeSpeed: 50,
   		backSpeed: 50,
    	loop: true,
		smartBackspace: false,
    });
	
});


