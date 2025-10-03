document.addEventListener('DOMContentLoaded', () => {
    const textInput = document.getElementById('text-input');
    const output = document.getElementById('output');
    const modeSwitch = document.getElementById('mode-switch');
    const encodeOptions = document.getElementById('encode-options');
    const emojiPicker = document.getElementById('emoji-picker');
    const letterPicker = document.getElementById('letter-picker');
    const switchLabels = document.querySelectorAll('.switch-container label');

    const emojis = ['😀', '😂', '🥰', '😎', '🤔', '👍', '👎', '👏', '😅', '🤝', '🎉', '🎂', '🍕', '🌈', '🌞', '🌙', '🔥', '💯', '🚀', '👀', '💀', '🥹'];
    const letters = 'abcdefghijklmnopqrstuvwxyz'.split('');
    // Initialize selectedCarrier to the first emoji by default
    let selectedCarrier = emojis[0]; 
    
    // Define the invisible characters used for encoding
    const ZERO_WIDTH_SPACE = '\u200B'; // Represents '1'
    const ZERO_WIDTH_NON_JOINER = '\u200C'; // Represents '0'
    const CHARACTER_DELIMITER = '\u200D'; // Separates encoded characters

    function populatePicker(picker, items, isDefault) {
        picker.innerHTML = ''; 
        items.forEach((item, index) => {
            const span = document.createElement('span');
            span.textContent = item;
            span.addEventListener('click', () => {
                // Remove selected class from all items in both pickers
                document.querySelectorAll('.picker span').forEach(el => el.classList.remove('selected-carrier'));
                // Add selected class to the clicked one
                span.classList.add('selected-carrier');
                selectedCarrier = item;
                updateOutput();
            });
            picker.appendChild(span);
            // Select the first emoji as default on initialization
            if (isDefault && index === 0) {
                span.classList.add('selected-carrier');
            }
        });
    }

    // --- Core Encoding Logic ---
    function encode(text, carrier) {
        // Now checks if text is empty, but ensures carrier is always defined (by default initialization)
        if (!text || !carrier) {
            // Return only the carrier if there's no text to encode
            return carrier || ''; 
        }
        
        let encodedBinary = '';
        for (let i = 0; i < text.length; i++) {
            const charCode = text.charCodeAt(i);
            const binary = charCode.toString(2);
            
            // Convert binary to invisible characters
            encodedBinary += binary.replace(/0/g, ZERO_WIDTH_NON_JOINER)
                                .replace(/1/g, ZERO_WIDTH_SPACE) 
                                + CHARACTER_DELIMITER;
        }

        // Return the visible carrier + the invisible code
        return carrier + encodedBinary; 
    }

    // --- Core Decoding Logic ---
    function decode(encodedText) {
        if (!encodedText) {
            return '';
        }

        const zwRegex = new RegExp(`[${ZERO_WIDTH_SPACE}${ZERO_WIDTH_NON_JOINER}]`);
        const startOfHiddenMessage = encodedText.search(zwRegex);
        
        if (startOfHiddenMessage === -1) {
            return '';
        }
        
        const hiddenSequence = encodedText.substring(startOfHiddenMessage);

        const encodedChars = hiddenSequence.split(CHARACTER_DELIMITER).filter(s => s.length > 0);
        
        let decodedText = '';
        encodedChars.forEach(encodedChar => {
            const binary = encodedChar.replace(new RegExp(ZERO_WIDTH_NON_JOINER, 'g'), '0')
                                    .replace(new RegExp(ZERO_WIDTH_SPACE, 'g'), '1');
            
            const charCode = parseInt(binary, 2);
            
            // FIX: Ensure the character code is a printable character (ASCII 32 or higher)
            // This prevents decoding control characters like , , etc.
            if (charCode >= 32) {
                 decodedText += String.fromCharCode(charCode);
            } else if (charCode > 0) {
                 // For codes 1-31, skip or replace. We'll skip to prevent garbage output.
                 // This ensures unprintable characters are ignored.
            }
        });

        return decodedText;
    }


    function updateOutput() {
        let result;
        const isEncodeMode = modeSwitch.checked; 

        if (isEncodeMode) {
            // ENCODE MODE
            result = encode(textInput.value, selectedCarrier);
        } else {
            // DECODE MODE
            result = decode(textInput.value);
        }
        
        if (output.value !== result) {
            output.value = result;
            if(result) {
                output.classList.add('highlight');
                setTimeout(() => {
                    output.classList.remove('highlight');
                }, 700);
            }
        }
    }

    function setMode() {
        // modeSwitch.checked is TRUE when the toggle is on the right ("Encode")
        const isEncodeMode = modeSwitch.checked; 
        
        // Label indices: [0] = Decode, [1] = Encode

        if (isEncodeMode) {
            // UI logic for ENCODE mode (switch is ON/checked)
            textInput.placeholder = "Enter text to encode";
            encodeOptions.classList.remove('hidden'); // SHOW picker options
            
            // Highlight 'Encode' (index 1) and fade 'Decode' (index 0)
            switchLabels[0].classList.remove('fw-bold'); 
            switchLabels[1].classList.add('fw-bold');    
        } else {
            // UI logic for DECODE mode (switch is OFF/unchecked)
            textInput.placeholder = "Paste encoded text to decode";
            encodeOptions.classList.add('hidden'); // HIDE picker options
            
            // Highlight 'Decode' (index 0) and fade 'Encode' (index 1)
            switchLabels[0].classList.add('fw-bold');    
            switchLabels[1].classList.remove('fw-bold'); 
        }
        
        // Reset inputs and update output to reflect the mode change immediately
        textInput.value = '';
        output.value = '';
        updateOutput(); 
    }
    
    // Event Listeners
    textInput.addEventListener('input', updateOutput);
    modeSwitch.addEventListener('change', setMode);

    // Initial setup
    populatePicker(emojiPicker, emojis, true);
    populatePicker(letterPicker, letters, false);
    
    // Ensure the switch starts in DECODE mode (unchecked)
    modeSwitch.checked = false; 
    setMode();
});