MyReddit.Collections.Posts = Backbone.Collection.extend({
  model: MyReddit.Models.Post,
  url: "/api/v1/post/"
});
