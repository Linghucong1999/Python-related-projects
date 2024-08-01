const crypto = require('crypto-js');

const key = "NLgz5CquFlFiUIcY"

const date = unescape(encodeURIComponent(new Date().getTime()));

const date_array = crypto.enc.Utf8.parse(date);
const key_hash = crypto.enc.Utf8.parse(key);
const value = crypto.AES.encrypt(date_array, key_hash, {
    mode: crypto.mode.ECB,
})

console.log(value.toString())