MyReddit.Routers.Router = Backbone.Router.extend({
  routes: {
    "": "index",
  },

  initialize: function (options) {
    this.$rootEl = options.$rootEl;
  },

  index: function () {
    subs = new MyReddit.Collections.Subs()
    subs.fetch({
      success: function (collection) {
        view = new MyReddit.Views.SubsIndex({ collection: collection })
        this._swapView(view)
      }.bind(this)
    })
  },

  _swapView: function (view) {
    this._currentView && this._currentView.remove();
    this._currentView = view;
    this.$rootEl.html(view.render().$el);
  }
});
