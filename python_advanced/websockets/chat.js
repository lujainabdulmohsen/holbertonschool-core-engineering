const socket = new WebSocket('ws://localhost:8000/ws');
const form = document.getElementById('chat-form');
const input = document.getElementById('message');
const messages = document.getElementById('messages');

form.addEventListener('submit', (event) => {
  event.preventDefault();

  if (input.value.trim() && socket.readyState === WebSocket.OPEN) {
    socket.send(input.value);
    input.value = '';
  }
});

socket.addEventListener('message', (event) => {
  const message = document.createElement('p');
  message.textContent = event.data;
  messages.appendChild(message);
});
