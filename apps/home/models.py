from django.db import models

from wagtail.admin.panels import FieldPanel
from wagtail.models import Page
from wagtail.fields import StreamField
from modelcluster.fields import ParentalManyToManyField

from .blocks import AboutBlock


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
        AboutBlock(),
        use_json_field=True,
        blank=True,
    )
    featured_projects = ParentalManyToManyField(
        "projects.ProjectPage",
        blank=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("hero_title"),
        FieldPanel("hero_role"),
        FieldPanel("hero_image"),
        FieldPanel("about_content"),
        FieldPanel("featured_projects"),
    ]
