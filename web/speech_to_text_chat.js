
var is_running = false
const mic_button = document.getElementById("mic_button")
mic_button.addEventListener("click", function(){
    mic_button.style.backgroundColor = "#00ffbf"
    eel.main()
})


eel.expose(welcomeMessage)
function welcomeMessage(text){
    let chat_messages_div = document.getElementById("chat_messages")
    let welcome_message_div = document.createElement("div")
    welcome_message_div.innerHTML += text;
    welcome_message_div.className = "systemMessageClass"
    chat_messages_div.appendChild(welcome_message_div)
    const chat_area_div = document.getElementById("chat_area")
    chat_area_div.scrollTop = chat_area_div.scrollHeight
}


eel.expose(askMessage)
function askMessage(text){
    let chat_messages_div = document.getElementById("chat_messages")
    let ask_message_div = document.createElement("div")
    ask_message_div.innerHTML += text;
    ask_message_div.className = "systemMessageClass"
    chat_messages_div.appendChild(ask_message_div)
    const chat_area_div = document.getElementById("chat_area")
    chat_area_div.scrollTop = chat_area_div.scrollHeight
}


eel.expose(assistantMessage)
function assistantMessage(response){
    let chat_messages_div = document.getElementById("chat_messages")
    let assistant_message_div = document.createElement("div");
    assistant_message_div.innerHTML += response;
    assistant_message_div.className = "assistantMessageClass"
    chat_messages_div.appendChild(assistant_message_div)
    const chat_area_div = document.getElementById("chat_area")
    chat_area_div.scrollTop = chat_area_div.scrollHeight
}


eel.expose(userMessage)
function userMessage(response){
    let chat_messages_div = document.getElementById("chat_messages")
    let user_message_div = document.createElement("div");
    user_message_div.innerHTML += response;
    user_message_div.className = "userMessageClass"
    chat_messages_div.appendChild(user_message_div)
    const chat_area_div = document.getElementById("chat_area")
    chat_area_div.scrollTop = chat_area_div.scrollHeight
}


eel.expose(goodbyeMessage)
function goodbyeMessage(text){
    let chat_messages_div = document.getElementById("chat_messages")
    let goodbye_message_div = document.createElement("div")
    goodbye_message_div.innerHTML += text;
    goodbye_message_div.className = "systemMessageClass"
    chat_messages_div.appendChild(goodbye_message_div)
    const chat_area_div = document.getElementById("chat_area")
    mic_button.style.backgroundColor = "#217aff00"
    chat_area_div.scrollTop = chat_area_div.scrollHeight
}


function send_text_message(){
    let message_input = document.getElementById("message_input")
    let text_message = message_input.value.trim()
    if (text_message != ""){
        eel.text_message_response(text_message)
        message_input.value = ""
    }
}

let send_button = document.getElementById("send_button")
send_button.addEventListener("click", send_text_message)

document.getElementById("message_input").addEventListener("keydown", (event)=>{
    if(event.key === "Enter"){
        event.preventDefault();
        send_text_message()
    } 

})

let menu_list = document.getElementById("menu_list")
let menu_button = document.getElementById("menu")
menu_button.addEventListener("click", function(){
    menu_list.style.visibility = "visible"
    menu_button.style.visibility= "hidden"
})

let close_menu_btn = document.getElementById("close_menu_button")
close_menu_btn.addEventListener("click", function(){
    menu_list.style.visibility = "hidden"
    menu_button.style.visibility = "visible"
})


var selected_language = "English"

// let languages = ["English", "Hindi", "Japanese", "German", "French", "Marathi", "Italian", "Punjabi"]
let languages = ['English', 'Chinese', 'German', 'Spanish', 'Russian', 'Korean', 'French', 'Japanese', 'Portuguese', 'Turkish', 'Polish', 'Catalan', 'Dutch', 'Arabic', 'Swedish', 'Italian', 'Indonesian', 'Hindi', 'Finnish', 'Vietnamese', 'Hebrew', 'Ukrainian', 'Greek', 'Malay', 'Czech', 'Romanian', 'Danish', 'Hungarian', 'Tamil', 'Norwegian', 'Thai', 'Urdu', 'Croatian', 'Bulgarian', 'Lithuanian', 'Latin', 'Maori', 'Malayalam', 'Welsh', 'Slovak', 'Telugu', 'Persian', 'Latvian', 'Bengali', 'Serbian', 'Azerbaijani', 'Slovenian', 'Kannada', 'Estonian', 'Macedonian', 'Breton', 'Basque', 'Icelandic', 'Armenian', 'Nepali', 'Mongolian', 'Bosnian', 'Kazakh', 'Albanian', 'Swahili', 'Galician', 'Marathi', 'Punjabi', 'Sinhala', 'Khmer', 'Shona', 'Yoruba', 'Somali', 'Afrikaans', 'Occitan', 'Georgian', 'Belarusian', 'Tajik', 'Sindhi', 'Gujarati', 'Amharic', 'Yiddish', 'Lao', 'Uzbek', 'Faroese', 'Haitian creole', 'Pashto', 'Turkmen', 'Nynorsk', 'Maltese', 'Sanskrit', 'Luxembourgish', 'Myanmar', 'Tibetan', 'Tagalog', 'Malagasy', 'Assamese', 'Tatar', 'Hawaiian', 'Lingala', 'Hausa', 'Bashkir', 'Javanese', 'Sundanese', 'Cantonese']
let languages_btn = document.getElementById("languages")
let settings_btn = document.getElementById("settings")
languages_btn.addEventListener("click", function(){
    
    settings_btn.style.display = "none"
    let language_list = document.createElement("div")
    language_list.className = "language_list"
    menu_list.appendChild(language_list)
    languages.forEach(function(lang){
        let lang_radio_div = document.createElement("div")
        lang_radio_div.className = "lang_radio_div_cls"

        let lang_radio = document.createElement("input")
        lang_radio.className = "lang_radio_cls"
        lang_radio.type = "radio"
        lang_radio.name = "lang_name"
        lang_radio.value = lang

        let lang_radio_label = document.createElement("label")
        lang_radio_label.className = "lang_radio_label_cls"
        lang_radio_label.innerHTML = lang

        lang_radio_div.appendChild(lang_radio)
        lang_radio_div.appendChild(lang_radio_label)
        language_list.appendChild(lang_radio_div)
    })

    let confirm_lang_btn = document.createElement("button")
    confirm_lang_btn.id = "confirm_lang_btn"
    confirm_lang_btn.innerHTML = "Confirm"
    menu_list.appendChild(confirm_lang_btn)
    confirm_lang_btn.addEventListener("click", function(){
        let selected_lang_list = document.getElementsByName("lang_name")
        selected_lang_list.forEach(function(lang){
            if(lang.checked){
                // console.log(lang.value)
                // eel.getSelectedLanguage(lang.value)
                selected_language = lang.value
            }
        })
        language_list.style.display = "none"
        confirm_lang_btn.style.display = "none"
        settings_btn.style.display = "flex"
    })
})

eel.expose(getSelectedLanguage)
function getSelectedLanguage(){
    return selected_language;
}