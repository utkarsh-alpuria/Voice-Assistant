
const start_stop_btn = document.getElementById("start_stop")
start_stop_btn.addEventListener("click", function(){
    eel.start_stop_function()
})

eel.expose(is_running_true)
function is_running_true(){
    const start_stop_btn = document.getElementById("start_stop")
    start_stop_btn.style.borderColor = "#00ffbf"
    start_stop_btn.style.backgroundColor = "#00ffbf"
}

eel.expose(is_running_false)
function is_running_false(){
    const start_stop_btn = document.getElementById("start_stop")
    start_stop_btn.style.borderColor = "#ffffff"
    start_stop_btn.style.backgroundColor = "transparent"
    const text_message = document.getElementById("text_message")
    text_message.style.visibility = "hidden"
}

eel.expose(showListening)
function showListening(){
    const text_message = document.getElementById("text_message")
    text_message.style.visibility = "visible"
}


eel.expose(jarvisActivated)
function jarvisActivated(){
    const text_message = document.getElementById("text_message")
    text_message.textContent = "JARVIS\r\nActive"
    eel.response_to_audio("jarvis activated")
    setTimeout(showChatScreen, 3000)
}

function showChatScreen(){
    var chat_screen = document.getElementById("chat_screen")
    var wake_word_screen = document.getElementById("wake_word_screen")
    if(chat_screen.style.display == "none"){
        wake_word_screen.style.display = "none"
        chat_screen.style.display = "block"
        eel.welcome()
        eel.start_stop_function()
    }
    else{
        wake_word_screen.style.display = "block"
        chat_screen.style.display = "none"
    }
}