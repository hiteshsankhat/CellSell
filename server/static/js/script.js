function searchOpen() {
    var search = $('#txtSearch').val();
    var data = {
        search: search
    };
    $.ajax({
        url: '/autocomplete-search',
        data: data,
        dataType: 'json',
        success: function (data) {
            const dataList = document.getElementById('phoneList');
            while (dataList.firstChild) {
                dataList.removeChild(dataList.firstChild);
            }
            data.data.forEach(element => {
                const option = document.createElement('option');
                option.setAttribute('value', element);
                dataList.appendChild(option);
            });
        }
    });
}

function searchOperations() {
    var search = $('#txtSearch').val();
    var data = {
        search: search
    };
    $.ajax({
        url: '/get-search-result',
        data: data,
        dataType: 'json',
        success: function (data) {
            var url = "";
            if (data.data.length == 1) {
                url = window.location.origin + "/varient/" + data.data[0];
            } else {
                url = window.location.origin + "/not-found-page";
            }
            window.location.replace(url);
        }
    });
}

$("#fun_cond_continue_btn").click(function (e) {
    $("#first_block").addClass('hide-block');
    $("#function_condition_blk").removeClass('hide-block');
    e.preventDefault();
});

$("#fun_cond_next_btn").click(function (e) {
    var issueNoIssueValue = $("input[name='issue_no_issue']:checked").val();
    if (issueNoIssueValue != 2 && issueNoIssueValue) {
        $("#function_condition_blk").addClass('hide-block');
        $("#accessories_block").removeClass('hide-block');
    }
    if (issueNoIssueValue == 2) {
        $("#give_final_price").append("0.00");
        $("#function_condition_blk").addClass('hide-block');
        $("#final_block").removeClass('hide-block');
    }
    e.preventDefault();
});


$("#accessories_next_btn").click(function (e) {
    var charger = $("input[name='charger']:checked").val();
    var earPhone = $("input[name='ear_phone']:checked").val();
    var box = $("input[name='box']:checked").val();
    $("#accessories_block").addClass('hide-block');
    $("#bill_condition_blk").removeClass('hide-block');
    e.preventDefault();
});

$("#accessories_previous_btn").click(function (e) {
    $("#accessories_block").addClass('hide-block');
    $("#function_condition_blk").removeClass('hide-block');
    e.preventDefault();
});

$("#bill_next_btn").click(function (e) {
    var billStatus = $("input[name='valid_bill_status']:checked").val();
    if (billStatus) {
        $("#bill_condition_blk").addClass('hide-block');
        $("#phone_condition_blk").removeClass('hide-block');
    }
    e.preventDefault();
});


$("#bill_previous_btn").click(function (e) {
    $("#bill_condition_blk").addClass('hide-block');
    $("#accessories_block").removeClass('hide-block');
    e.preventDefault();
});

$("#phone_cond_next_btn").click(function (e) {
    var status = $("input[name='phone_overall_condition']:checked").val();
    if (status) {
        var issueNoIssueValue = $("input[name='issue_no_issue']:checked").val();
        var charger = $("input[name='charger']:checked").val();
        var earPhone = $("input[name='ear_phone']:checked").val();
        var box = $("input[name='box']:checked").val();
        var billStatus = $("input[name='valid_bill_status']:checked").val();

        if (issueNoIssueValue === "no_issue") issueNoIssueValue = $("#hidden_issue_no_issue").val();
        if (charger) charger = $("#hidden_has_charger").val();
        if (earPhone) earPhone = $("#hidden_ear_phone").val();
        if (box) box = $("#hidden_box").val();
        if (billStatus === "billBelow") billStatus = $("#hidden_bill_below").val();
        if (billStatus === "billAbove") billStatus = $("#hidden_bill_above").val();
        if (status === "new") status = $("#hidden_phone_new").val();
        if (status === "fair") status = $("#hidden_phone_fair").val();
        if (status === "excellent") status = $("#hidden_phone_excellent").val();

        var result = parseFloat(issueNoIssueValue) +
            parseFloat((charger ? charger : 0)) +
            parseFloat((earPhone ? earPhone : 0)) +
            parseFloat((box ? box : 0)) +
            parseFloat(billStatus) +
            parseFloat(status);
        $("#give_final_price").append(result);
        $("#phone_condition_blk").addClass('hide-block');
        $("#final_block").removeClass('hide-block');
    }
    e.preventDefault();
});


$("#phone_cond_previous_btn").click(function (e) {
    $("#phone_condition_blk").addClass('hide-block');
    $("#bill_condition_blk").removeClass('hide-block');
    e.preventDefault();
});


//// import from excel part 

function importExcel(event) {
    document.getElementById('upload').click();
}

$("#upload").on("change", function () {
    document.getElementById('formSubmit').click();
});


$('#id_ajax_upload_form').submit(function(e){
    e.preventDefault();
    $form = $(this)
    var formData = new FormData(this);
    $.ajax({
        url: '/import-data-from-excel',
        type: 'POST',
        data: formData,
        success: function (response) {
            console.log('done');
            $('#upload').val('');
            location.reload(true);
        },
        cache: false,
        contentType: false,
        processData: false
    });
});