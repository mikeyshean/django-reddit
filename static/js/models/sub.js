MyReddit.Models.Sub = Backbone.Model.extend({
  urlRoot: function () {
    return "/api/v1/sub/";
  },

  parse: function (resp) {
    if (resp && resp.posts) {
      this.posts().set(resp.posts)
    }
    delete resp.posts

    return resp
  },

  posts: function () {
    if (!this._posts) {
      this._posts = new MyReddit.Collections.Posts()
    }
    return this._posts
  }
});
