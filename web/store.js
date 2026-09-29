import { EMPTY_CONFIG } from "./config.js";

export let config = structuredClone(EMPTY_CONFIG);

export function setConfig(next){
    config = next;
}