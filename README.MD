# ✨ Emoji Encoder: Hide Messages in Plain Sight ✨

Welcome to the Emoji Encoder project\! This is a fun and simple web tool that allows you to hide secret messages within a string of emojis or alphabet letters. It uses a clever encoding technique to make your message invisible to the naked eye, allowing you to share confidential text in a playful and unconventional way. 🤫

-----

## ⚙️ How It Works

This tool operates on a simple but effective principle: it takes your text and a selected "carrier" emoji or letter, then encodes the text by manipulating the Unicode character codes.

  * **Encoding:** When you enter text and select a carrier, the `encode()` function in `script.js` converts each character of your message into its Unicode code point. It then adds the code point of the carrier to each of these. The final output is the carrier followed by this new sequence of characters, which looks like a string of random emojis or letters.
  * **Decoding:** The `decode()` function reverses this process. It takes the first character of the input (the carrier), gets its code point, and then subtracts that code point from each subsequent character in the string. The result is your original, hidden message.

The project also uses a smooth CSS transition to hide or show the emoji and letter pickers, depending on whether you are in "encode" or "decode" mode.

-----

## 💡 Use Cases

This tool isn't just a toy\! It can be used for:

  * **Fun & Games:** Send cryptic messages to friends who also have the decoder. 🤪
  * **Light-hearted "Secret" Sharing:** Share private information without it looking suspicious.
  * **Educational Purposes:** A great way to learn about character encoding and JavaScript. 👨‍💻

-----

## 📂 File Structure

The project is organized into a clean and easy-to-understand folder structure:

```
emoji-encoder REPO
├── emoji-encoder/
│   ├── index.html       
│   ├── script.js        
│   └── style.css        
```

-----

## 🔧 Technology Stack

This project is built using standard web technologies:

  * **HTML5:** For the structure of the web page.
  * **CSS3:** For styling and animations.
  * **JavaScript (ES6):** For all the encoding, decoding, and user interaction logic.
  * **Bootstrap 5:** A CSS framework for responsive design and UI components.
  * **Google Fonts:** Specifically, the `Inter` font for a clean typographic look.

-----

## ⚙️ Requirements

All you need to run this project is a modern web browser like Chrome, Firefox, or Safari. No other installations or configurations are required.

-----

## ▶️ How to Run

Running the project is as simple as opening a file\!

1.  **Download:** Download the `emoji-encoder.zip` file.
2.  **Unzip:** Extract the contents of the zip file.
3.  **Open:** Locate the `index.html` file and open it with your web browser.

That's it\! The application will load immediately, and you can start encoding and decoding your messages. 🎉

-----

## ▶️ Working video

![Working Video of emoji encoder](emoji-encoder.mp4)

-----

## 💖 Author

[Nitin Kumar](https://linkedin.com/in/nitin30kumar/)

