MyReddit.Views.SubsIndex = Backbone.View.extend({
  template: JST.subs_index,

  render: function () {
    this.$el.html(this.template({ subs: this.collection }));
    return this;
  }
});
