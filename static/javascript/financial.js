function display_data() {
    var error_msg_class = document.getElementById("error_msg").className;
    if (error_msg_class == "instructions error_true") {
        document.getElementById("error_msg").style.removeProperty("display");
        document.getElementsByClassName("top_section")[0].style.display = "none";
    }
}

function show_graph(elem) {
    var parent_div = elem.parentElement.parentElement.childNodes
    parent_div[1].querySelectorAll("button")[0].className = "selected_btn"
    parent_div[1].querySelectorAll("button")[1].className = ""
    parent_div[5].style.display = "none";
    parent_div[3].style.removeProperty("display");
}

function show_table(elem) {
    var parent_div = elem.parentElement.parentElement.childNodes

    parent_div[1].querySelectorAll("button")[0].className = ""
    parent_div[1].querySelectorAll("button")[1].className = "selected_btn"
    parent_div[5].style.removeProperty("display");
    parent_div[3].style.display = "none";

    elem.className = "selected_btn";
}