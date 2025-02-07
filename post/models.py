from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.search import index
from wagtail.admin.panels import FieldPanel


class PostPage(Page):
    parent_page_types = ["home.HomePage"]
    body = RichTextField(blank=True)
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Post Image",
    )

    search_fields = Page.search_fields + [
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('image'),
        FieldPanel('body'),
    ]
