from django.db import models

from wagtail import blocks
from wagtail.admin.panels import FieldPanel
from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.images.blocks import ImageChooserBlock


class HomePage(Page):
    hero_title = models.CharField(max_length=120, blank=True, help_text="Your name")
    hero_role = models.CharField(
        max_length=120, blank=True, help_text="Your occupation"
    )
    hero_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    about_content = StreamField(
        [
            ("heading", blocks.CharBlock()),
            ("paragraph", blocks.RichTextBlock()),
            ("image", ImageChooserBlock()),
            ("quote", blocks.BlockQuoteBlock()),
        ],
        use_json_field=True,
        blank=True,
    )

    show_projects_section = models.BooleanField(default=True)

    content_panels = Page.content_panels + [
        FieldPanel("hero_title"),
        FieldPanel("hero_role"),
        FieldPanel("hero_image"),
        FieldPanel("about_content"),
        FieldPanel("show_projects_section"),
    ]
