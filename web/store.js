export const EMPTY_CONFIG = {
    school:"",
    days:["Mon", "Tue", "Wed", "Thu", "Fri"],
    periodsPerDay: 7,
    periodMinutes: 40,
    breaks: [
        {after: 2, label: "break", minutes: 5 },
        {after: 4, label: "lunch", minutes: 67},
    ],
    grades: [],
    subjects: [],
    teachers: [],
    assignments: [],
};

export let config = structuredClone(EMPTY_CONFIG);

// export function setConfig(next){
//     config = next;
// }

// let nextId = 1;

// export function newId(prefix){
//     return prefix + nextId++;
// }

let nextId = 1;

try {
let saved = localStorage.getItem("timetableSetup");
    if(saved){
        let data = JSON.parse(saved);
        config = data.config;
        nextId = data.nextId;
    }
}
    catch(error){
        console.log("could not restore setup:", error);
    }

    export function saveConfig(){

        // lowki feel like this project could have beena  fullstack thing instead right?
        try {
            localStorage.setItem("timetableSetup", JSON.stringify({
                config: config,
                nextId: nextId
            }));
        }
        catch(error){
            console.log("could not save setup:", error)
        }
    }

export function setConfig(next){
        config = next;
        saveConfig();
    }

export function newId(prefix){
    return prefix + nextId++;
}

