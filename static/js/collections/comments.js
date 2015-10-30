MyReddit.Collections.Comments = Backbone.Collection.extend({
  model: MyReddit.Models.Comment,
  url: "/api/v1/comment/"
});
