 /* function */
 let loadForm = function () {
  let btn = $(this);
  $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
          $("#modal-livestock").modal("show");
      },
      success: function (data) {
          $("#modal-livestock .modal-content").html(data.html_form);
      }
  });
};
let saveForm = function () {
  let form = $(this);
  $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
          if (data.form_is_valid) {
              $("#book-table tbody").html(data.html_book_list);
              $("#modal-livestock").modal("hide");
          }
          else {
              $("#modal-livestock .modal-content").html(data.html_form);
          }
      }
  });
  return false;
};

/* Binding */

// create livestock
$(".js-create-livestock").click(loadForm);
$("#modal-livestock").on("submit", ".js-livestock-create-form", saveForm);

// // Update livestock
// $("#book-table").on("click", ".js-update-book", loadForm);
// $("#modal-book").on("submit", ".js-book-update-form", saveForm);

// // Delete livestock 
// $("#book-table").on("click", ".js-delete-book", loadForm);
// $("#modal-book").on("submit", ".js-book-delete-form", saveForm);

// js for date picker
$(document).ready(function() {
    $('#js-date').datepicker();
});
