const express = require("express");
const app = express();
app.use(express.json());

function cipher(text, shift) {
    let result = "";

    for (let char of text) {
        if (/[a-zA-Z]/.test(char)) {
            let base = char === char.toUpperCase() ? 65 : 97;
            let code = char.charCodeAt(0) - base;
            result += String.fromCharCode((code + shift) % 26 + base);
        } else {
            result += char;
        }
    }

    return result;
}

app.post("/encrypt", (req, res) => {
    const { text, shift } = req.body;
    res.json({ result: cipher(text, shift) });
});

app.post("/decrypt", (req, res) => {
    const { text, shift } = req.body;
    res.json({ result: cipher(text, -shift) });
});

app.listen(3000, () => console.log("Server running on port 3000"));
