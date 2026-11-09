
// so this is a fake timetable
// whole latta copy paste 

export let schedule = {};

try {
    const saved = localStorage.getItem("timetableSchedule");
    if (saved){
        schedule = JSON.parse(saved);
    }
}
catch (error){
    console.log("cant restore timetable for some reason", error)
}



// bruh idk, might change, idk, this shi is so confusing
export function setSchedule(source) {
    schedule = source;
    localStorage.setItem("timetableSchedule", JSON.stringify(schedule));
}