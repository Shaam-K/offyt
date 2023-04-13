var select_text = document.getElementById('sel_desel_text');


var sel = false;


var check_required = true;

function no_of_checks() {
    var check_count = 0;
    var ele_count=document.querySelectorAll(".video_check");

    for(var i=0; i<ele_count.length; i++) {

        if(ele_count[i].type == 'checkbox' && ele_count[i].checked == true) {
            check_count++;
        }

    }

    if (check_count > 0) {
        check_required = false;
    }
}

function required_toggle() {
    const input_check = document.getElementById('first_name');
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