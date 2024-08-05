const crypto = require('crypto-js');

const key = "NLgz5CquFlFiUIcY"

const timestamp = new Date().getTime();
const date = new Date(timestamp).toLocaleString().replace(/\//g, '-');
const [year, month, day] = date.split(/-|\s/);
const time = date.split(' ')[1];
const monthFormatted = String(month).padStart(2, '0');
const dayFormatted = String(day).padStart(2, '0');
const timeSplit = time.split(':');
const hour = String(timeSplit[0]).padStart(2, '0');
const minute = String(timeSplit[1]).padStart(2, '0');
const second = String(timeSplit[2]).padStart(2, '0');
const formattedDate = `${year}-${monthFormatted}-${dayFormatted} ${hour}:${minute}:${second}`;

const date_array = crypto.enc.Utf8.parse(date);
const key_hash = crypto.enc.Utf8.parse(key);
const value = crypto.AES.encrypt(date_array, key_hash, {
    mode: crypto.mode.ECB,
}).toString();

console.log(value)
// 2024-08-05 11:08:35