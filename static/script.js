
// Message (dans la console) si quelqu'un se connecte
const socket = io();
let username = null;

socket.on("connect", () => {
  console.log("Un joueur s'est connecté !");
});

/**
 * @todo afficher wordInput juste après userInput.remove()
 */
userInput = document.querySelector("#username_input")
userInput.addEventListener('keydown', (input) => {
  if (input.key === 'Enter') {
    username = userInput.value.trim()
    if (username) {  // Seulement si non vide
      socket.emit('set_username', {username})
      userInput.remove()
    }
  }
})


// Envoi l'input du joueur au serveur
wordInput = document.querySelector("#wordInput");

wordInput.addEventListener("keydown", (input) => {
  if (input.key === 'Enter') {
    const word = wordInput.value.trim()
    socket.emit('submit_word', {word})
    wordInput.value = ''
  }
});

// Endroit qui affiche les mots écrits
inputZone = document.querySelector("#input_zone")

socket.on('word_result', (e) =>{
  const newElement = document.createElement('p')
  newElement.innerHTML = e
  inputZone.appendChild(newElement);
})