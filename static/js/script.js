// Initialize Materialize Elements
$(document).ready(function(){
    $(".sidenav").sidenav();
    $(".collapsible").collapsible();
    $(".carousel").carousel();
    $("select").formSelect();
    $(".tooltipped").tooltip();
    $(".modal").modal();
    $("input#input_text, textarea#textarea2, textarea#recipe_description, textarea#basic_ingredients, textarea#complementary_ingredients, textarea#category_method"
).characterCounter();
    $(".cancel-form").click(function() {
        window.history.back();
    });
    

// Code provided from the explanatory videos from the Course 
    validateMaterializeSelect();
    function validateMaterializeSelect() {
        let classValid = { "border-bottom": "1px solid #4caf50", "box-shadow": "0 1px 0 0 #4caf50" };
        let classInvalid = { "border-bottom": "1px solid #f44336", "box-shadow": "0 1px 0 0 #f44336" };
        if ($("select.validate").prop("required")) {
            $("select.validate").css({ "display": "block", "height": "0", "padding": "0", "width": "0", "position": "absolute" });
        }
        $(".select-wrapper input.select-dropdown").on("focusin", function () {
            $(this).parent(".select-wrapper").on("change", function () {
                if ($(this).children("ul").children("li.selected:not(.disabled)").on("click", function () { })) {
                    $(this).children("input").css(classValid);
                }
            });
        }).on("click", function () {
            if ($(this).parent(".select-wrapper").children("ul").children("li.selected:not(.disabled)").css("background-color") === "rgba(0, 0, 0, 0.03)") {
                $(this).parent(".select-wrapper").children("input").css(classValid);
            } else {
                $(".select-wrapper input.select-dropdown").on("focusout", function () {
                    if ($(this).parent(".select-wrapper").children("select").prop("required")) {
                        if ($(this).css("border-bottom") != "1px solid rgb(76, 175, 80)") {
                            $(this).parent(".select-wrapper").children("input").css(classInvalid);
                        }
                    }
                });
            }
        });
    }
});

// Code approach with help from former students and improved
// Add and Remove Ingredients
 var ingredientField = $(".ingredient").length;
    $("#add_ingredient").on("click", function () {
        $("select").formSelect("destroy");
        $(".ingredient:first").clone().insertBefore("#add_ingredient").val("");
        $("select").formSelect();
        ingredientField += 1;
    });

    $("#remove_ingredient").on("click", function () {
        if (ingredientField > 1) {
            /* only to remove the :last item */
            $(".ingredient:last").remove();
            /* it ensures original ingredient line never gets deleted */
            ingredientField-= 1;
        }
    });   

// Add and Remove Extra Ingredients 
 var extraIngredientField = $(".compIngredient").length;
    $("#add_comp_ingredient").on("click", function () {
        $("select").formSelect("destroy");
        $(".compIngredient:first").clone().insertBefore("#add_comp_ingredient").val("");
        $("select").formSelect();
        extraIngredientField += 1;
    });

    $("#remove_comp_ingredient").on("click", function () {
        if (extraIngredientField > 1) {
            /* only to remove the :last item */
            $(".compIngredient:last").remove();
            /* it ensures original ingredient line never gets deleted */
            extraIngredientField-= 1;
        }
    });

// Add and Remove preparation steps
var preparationField = $(".new-step").length;
    /* add new cloned item */
    $("#add_step").on("click", function () {
        $(".new-step:first").clone().insertBefore("#add_step").val("");
        /* increase counter so original direction is never removed */
       preparationField += 1;
    });
    /* delete last cloned item */
    $("#remove_step").on("click", function () {
        if ( preparationField > 1) {
            /* only remove the :last item */
            $(".new-step:last").remove();
            /* ensure original direction line never gets deleted */
            preparationField-= 1;
        }
    });