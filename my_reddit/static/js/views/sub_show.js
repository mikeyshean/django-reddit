MyReddit.Views.SubShow = Backbone.View.extend({
  template: JST.subs_show,

  render: function () {
    this.$el.html(this.template({ sub: this.model }));
    return this;
  }
});
