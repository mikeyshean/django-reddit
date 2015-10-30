MyReddit.Models.Post = Backbone.Model.extend({
  urlRoot: function () {
    return "/api/v1/post/";
  }

});
