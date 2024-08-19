//Animator
const animator = (elem) => {
    switch (elem){
        case "ham":
            let class_name = elem+"_animator";
            $("."+elem).hasClass(class_name) ? $("."+elem).removeClass(elem+"_animator") : $("."+elem).addClass(class_name);
        break;
    }
}
