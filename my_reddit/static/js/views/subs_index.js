MyReddit.Views.SubsIndex = Backbone.View.extend({
  template: JST.subs_index,

  render: function () {
    console.log(this.collection);
    this.$el.html(this.template({ subs: this.collection }));
    return this;
  }
});
