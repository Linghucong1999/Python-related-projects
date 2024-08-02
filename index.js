const crypto = require('crypto-js');

const key = "NLgz5CquFlFiUIcY"

const timestamp = new Date().getTime();
const date = new Date(timestamp).toLocaleString().replace(/\//g, '-');
const date_array = crypto.enc.Utf8.parse(date);
const key_hash = crypto.enc.Utf8.parse(key);
const value = crypto.AES.encrypt(date_array, key_hash, {
    mode: crypto.mode.ECB,
}).toString();

console.log(value)