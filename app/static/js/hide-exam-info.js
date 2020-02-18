$("#score_exsort").on("change", function(){
                if(document.getElementById("score_exsort").value == 5){
                    $("#exam_info").show();
                    $("#show").show();
                }
                else{
                    $("#exam_info").hide();
                    $("#show").hide();
                }
            })