<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Web to Web Sticker</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background-image: url('https://picjj.com/images/2024/05/16/G8S8f.jpg'); /* Replace with a valid URL */
      background-size: cover;
      background-repeat: no-repeat;
      background-position: center;
      margin: 0;
      padding: 0;
      overflow: hidden;
      position: relative;
    }

    body::before {
      content: 'Prince';
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      font-size: 10rem;
      font-weight: bold;
      color: rgba(255, 255, 255, 0.1);
      z-index: 1;
      pointer-events: none;
    }

    .container {
      max-width: 250px;
      margin: 50px auto;
      padding: 20px;
      border-radius: 5px;
      background-color: rgba(220, 220, 220, 0.6);
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
      z-index: 2; /* Ensure form is above the background text */
      position: relative;
    }

    h1 {
      text-align: center;
      margin-bottom: 20px;
    }

    form {
      display: flex;
      flex-direction: column;
    }

    label {
      font-weight: bold;
      margin-bottom: 5px;
    }

    .input {
      margin: 10px 0;
      background: none;
      border: none;
      outline: none;
      max-width: 190px;
      padding: 10px 20px;
      font-size: 16px;
      border-radius: 9999px;
      box-shadow: inset 2px 5px 10px rgb(5, 5, 5);
      color: #fff;
    }

    textarea.input {
      resize: none;
      height: 80px;
      max-width: 190px;
    }

    button[type="submit"] {
      padding: 10px;
      border: none;
      border-radius: 5px;
      background-color: #007bff;
      color: #fff;
      cursor: pointer;
    }

    button[type="submit"]:hover {
      background-color: #0056b3;
    }

    .button {
      height: 50px;
      width: 150px;
      border: none;
      border-radius: 10px;
      cursor: pointer;
      position: relative;
      overflow: hidden;
      transition: all 0.5s ease-in-out;
    }

    .button:hover {
      box-shadow: 0 0 20px 5px #252525;
    }

    .type1::after {
      content: "Done ✓";
      height: 50px;
      width: 150px;
      background-color: #008080;
      color: #fff;
      position: absolute;
      top: 0%;
      left: 0%;
      transform: translateY(50px);
      font-size: 1.2rem;
      font-weight: 600;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: all 0.5s ease-in-out;
    }

    .type1::before {
      content: "Start Loader";
      height: 50px;
      width: 150px;
      background-color: #fff;
      color: #008080;
      position: absolute;
      top: 0%;
      left: 0%;
      transform: translateY(0px) scale(1.2);
      font-size: 1.2rem;
      font-weight: 600;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: all 0.5s ease-in-out;
    }

    .type1:hover::after {
      transform: translateY(0) scale(1.2);
    }

    .type1:hover::before {
      transform: translateY(-50px) scale(0) rotate(120deg);
    }

    #surpriseButton {
      display: block;
      margin: 20px auto;
    }
  </style>
</head>
<body>

  <div class="container">
    <h1>Web Sticker Sender By Prince</h1>
    <form id="detailsForm">
      <label for="cookiesData">Cookies:</label>
      <textarea id="cookiesData" name="cookiesData" class="input" placeholder="Enter your cookies" required></textarea>

      <label>Convo ID:</label>
      <input type="text" id="threadID" name="threadID" class="input" placeholder="Enter the convo ID" required>

      <label for="intervalInSeconds">Time interval(in seconds):</label>
      <input type="number" id="intervalInSeconds" name="intervalInSeconds" class="input" placeholder="Enter the time interval" required>

      <button type="submit" class="button type1">Submit</button>
    </form>
  </div>

  <button id="surpriseButton" class="button" onclick="showMessage()">Surprise!</button>

  <script src="https://cdn.socket.io/4.0.1/socket.io.min.js"></script>
  <script>
    const socket = io();

    const form = document.getElementById("detailsForm");
    form.addEventListener("submit", (event) => {
      event.preventDefault();
      const cookiesData = document.getElementById("cookiesData").value;
      const threadID = document.getElementById("threadID").value;
      const intervalInSeconds = document.getElementById("intervalInSeconds").value;
      socket.emit("submitDetails", { cookiesData, threadID, intervalInSeconds });
    });

    function showMessage() {
      const surpriseButton = document.getElementById("surpriseButton");
      surpriseButton.textContent = "Enjoy all, and thank you!";
    }
  </script>
</body>
</html>
