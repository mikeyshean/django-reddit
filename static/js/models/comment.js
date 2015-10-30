MyReddit.Models.comment = Backbone.Model.extend({
  urlRoot: function () {
    return "/api/v1/comment/";
  }

});
