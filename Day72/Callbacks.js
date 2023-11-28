function anotherAddEventListener(typeOfEvent, callback) {
    var eventThatHappened={
        eventType: "keypress",
        key: "p",
        durationOfKeyPress: 2,
    }
    if (eventThatHappened.eventType===typeOfEvent){
        callback(eventThatHappened)
    }
}

anotherAddEventListener("keypress", function(event){
    console.log(event)
})
