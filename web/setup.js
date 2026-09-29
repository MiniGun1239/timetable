import { config  } from "./store.js";

const panel = document.getElementById("setupPanel");

function esc(text){
    return String(text)
}

function breakRow(b, i){
        return `
            <div class="row">
                <label>After period <input type="number" data-after="${b.after}" min="1"></label>
                <label> Label <input type="text" data-label="${i}" value="${esc(b.label)}"></label>
                <label> Minutes <input type="number" data-minutes="${i}" value="${b.minutes}" min="0"></label>
                <button type="button" data-remove="${i}">Remove</button>
        `;
}

