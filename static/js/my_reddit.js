window.MyReddit = {
  Models: {},
  Collections: {},
  Views: {},
  Routers: {},
  initialize: function() {
    new MyReddit.Routers.Router({ $rootEl: $("#my-reddit") });
    Backbone.history.start();
  }
};
