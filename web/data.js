
// so this is a fake timetable
// whole latta copy paste 

export let schedule = {
    "11-A": {
        "Mon P1": { subject: "s1", teacher: "t1" },
        "Mon P2": { subject: "s2", teacher: "t2" },
        "Mon P3": { subject: "s1", teacher: "t1" },
        "Mon P4": { subject: "s3", teacher: "t3" },
        "Mon P5": { subject: "s1", teacher: "t1" },
        "Tue P1": { subject: "s2", teacher: "t2" },
        "Tue P2": { subject: "s1", teacher: "t1" },
        "Tue P3": { subject: "s3", teacher: "t3" },
        "Tue P4": { subject: "s2", teacher: "t2" },
        "Tue P5": { subject: "s4", teacher: "t4" },
        "Wed P1": { subject: "s1", teacher: "t1" },
        "Wed P2": { subject: "s3", teacher: "t3" },
        "Wed P3": { subject: "s2", teacher: "t2" },
        "Wed P4": { subject: "s1", teacher: "t1" },
        "Wed P5": { subject: "s4", teacher: "t4" },    

        // NOTE - I COPY PASTED EVERY LINE RQ. IDK IF THERE WOULD BE SOME PROBLEMS WITH HEARBEATS COUNTIN OR SMTH.
  },
  "11-B":{
        "Mon P1": { subject: "s2", teacher: "t2" },
        "Mon P2": { subject: "s1", teacher: "t1" },
        "Mon P3": { subject: "s4", teacher: "t4" },
        "Mon P4": { subject: "s2", teacher: "t2" },
        "Mon P5": { subject: "s3", teacher: "t3" },
        "Tue P1": { subject: "s1", teacher: "t1" },
        "Tue P2": { subject: "s3", teacher: "t3" },
        "Tue P3": { subject: "s2", teacher: "t2" },
        "Tue P4": { subject: "s1", teacher: "t1" },
        "Tue P5": { subject: "s4", teacher: "t4" },

  },
};

// ill remove this comments dw

export function setSchedule(source){

    let converted = {};

        Object.entries(source).forEach(function([className, days]){
            converted[className] = {};

            Object.entries(days).forEach(function([day, periods]){
                Object.entries(periods).forEach(function([period, lesson]){
                    converted[className][day + " " + period] = lesson;
                });
            });
        })
    schedule = converted;
}
