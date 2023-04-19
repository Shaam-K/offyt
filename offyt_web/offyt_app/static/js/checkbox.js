var select_text = document.getElementById('sel_desel_text');

var videos_checkbox = document.querySelectorAll(".video_check");

var sel = false;

var check_required = true;

var check_count = 0;

function no_of_checks() {

    for(var i=0; i<videos_checkbox.length; i++) {

        if(videos_checkbox[i].type == 'checkbox' && videos_checkbox[i].checked == true) {
            check_count++;
        }
    }
}


function select_all(){  
    var ele=document.querySelectorAll(".video_check");
    for(var i=0; i<ele.length; i++){  
        if(ele[i].type=='checkbox')  
            ele[i].checked=true;  
    }

    select_text.innerHTML = "Remove All";

    sel = true;
}

function deSelect(){  
    var ele=document.querySelectorAll(".video_check");
    for(var i=0; i<ele.length; i++){  
        if(ele[i].type=='checkbox')  
            ele[i].checked=false;  
    }
    select_text.innerHTML = "Select All";

    sel = false;
}

function toggle_sel_desel() {
    sel ? deSelect() : select_all();
}