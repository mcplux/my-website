from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.snippets.models import register_snippet
from wagtail.models import Page
from modelcluster.fields import ParentalManyToManyField


# Create your models here.
@register_snippet
class Skill(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    color = models.CharField(
        max_length=7,
        default="#10B981",
        help_text="Text color HEX (e.g. #3B82F6)",
    )

    def __str__(self):
        return self.name


class ProjectPage(Page):
    cover_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    description = models.TextField()

    skills = ParentalManyToManyField(
        "projects.Skill",
        blank=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("cover_image"),
        FieldPanel("description"),
        FieldPanel("skills"),
    ]


class ProjectsPage(Page):
    content = models.TextField()
    projects = ParentalManyToManyField(
        "projects.ProjectPage",
        blank=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("content"),
        FieldPanel("projects"),
    ]
