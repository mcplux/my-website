from django.db import models

from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField
from wagtail.snippets.models import register_snippet
from wagtail.models import Page
from modelcluster.fields import ParentalManyToManyField

from .blocks import ProjectLinkBlock, ProjectContentBlock


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

    description = models.TextField(help_text="Short description for previews")

    content = StreamField(
        ProjectContentBlock(),
        use_json_field=True,
        blank=True,
    )

    project_links = StreamField(
        (("link", ProjectLinkBlock()),),
        use_json_field=True,
        blank=True,
    )

    skills = ParentalManyToManyField(
        "projects.Skill",
        blank=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("cover_image"),
        FieldPanel("description"),
        FieldPanel("content"),
        FieldPanel("project_links"),
        FieldPanel("skills"),
    ]


class ProjectsPage(Page):
    def get_context(self, request):
        context = super().get_context(request)

        context["projects"] = (
            ProjectPage.objects.live().child_of(self).order_by("-first_published_at"),
        )[0]

        return context
