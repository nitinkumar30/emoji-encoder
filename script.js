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
    let selectedCarrier = null; 

    function populatePicker(picker, items, isDefault) {
        picker.innerHTML = ''; 
        items.forEach((item, index) => {
            const span = document.createElement('span');
            span.textContent = item;
            span.addEventListener('click', () => {
                document.querySelectorAll('.picker span').forEach(el => el.classList.remove('selected-carrier'));
                span.classList.add('selected-carrier');
                selectedCarrier = item;
                updateOutput();
            });
            picker.appendChild(span);
            if (isDefault && index === 0) {
                span.classList.add('selected-carrier');
                selectedCarrier = item;
            }
        });
    }

    // Rewritten encode/decode functions to use the carrier character
    function encode(text, carrier) {
        if (!text || !carrier) {
            return '';
        }
        let encodedText = '';
        const carrierCodePoint = carrier.codePointAt(0);
        
        for (let i = 0; i < text.length; i++) {
            const charCode = text.charCodeAt(i);
            const encodedCharCode = charCode + carrierCodePoint;
            const encodedChar = String.fromCodePoint(encodedCharCode);
            encodedText += encodedChar;
        }
        return carrier + encodedText;
    }

    function decode(encodedText) {
        if (!encodedText || encodedText.length < 2) {
            return '';
        }
        const carrier = encodedText[0];
        const carrierCodePoint = carrier.codePointAt(0);
        let decodedText = '';
        
        for (let i = 1; i < encodedText.length; i++) {
            const charCode = encodedText.codePointAt(i);
            const decodedCharCode = charCode - carrierCodePoint;
            decodedText += String.fromCharCode(decodedCharCode);
        }
        return decodedText;
    }

    function updateOutput() {
        let result;
        if (modeSwitch.checked) {
            result = decode(textInput.value);
        } else {
            result = encode(textInput.value, selectedCarrier);
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
        const isDecodeMode = modeSwitch.checked;
        
        if (isDecodeMode) {
            textInput.placeholder = "Paste encoded text to decode";
            encodeOptions.classList.add('hidden');
            switchLabels[0].classList.add('fw-bold');
            switchLabels[1].classList.remove('fw-bold');
        } else {
            textInput.placeholder = "Enter text to encode";
            encodeOptions.classList.remove('hidden');
            switchLabels[0].classList.remove('fw-bold');
            switchLabels[1].classList.add('fw-bold');
        }
        textInput.value = '';
        output.value = '';
    }
    
    // Event Listeners
    textInput.addEventListener('input', updateOutput);
    modeSwitch.addEventListener('change', setMode);

    // Initial setup
    populatePicker(emojiPicker, emojis, true);
    populatePicker(letterPicker, letters, false);
    setMode();
});