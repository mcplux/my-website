from django.db import models
from django.core.validators import MaxValueValidator

from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.fields import StreamField
from wagtail.models import Page, Orderable
from wagtail.snippets.models import register_snippet
from modelcluster.fields import ParentalManyToManyField, ParentalKey

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

    panels = [
        FieldPanel("name"),
        FieldPanel("slug"),
        FieldPanel("color"),
    ]

    def __str__(self):
        return self.name


class ProjectSkill(Orderable):
    page = ParentalKey(
        "projects.ProjectPage",
        related_name="project_skills",
        on_delete=models.CASCADE,
    )
    skill = models.ForeignKey(
        "projects.Skill",
        on_delete=models.CASCADE,
        related_name="+",
    )

    panels = [
        FieldPanel("skill"),
    ]


class ProjectPage(Page):
    weight = models.PositiveSmallIntegerField(
        default=0,
        validators=(MaxValueValidator(100),),
    )

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
        FieldPanel("weight"),
        FieldPanel("cover_image"),
        FieldPanel("description"),
        FieldPanel("content"),
        FieldPanel("project_links"),
        InlinePanel("project_skills", label="Skills"),
    ]


class ProjectsPage(Page):
    def get_context(self, request):
        context = super().get_context(request)

        projects = (
            ProjectPage.objects.live()
            .child_of(self)
            .order_by("-weight", "-first_published_at")
        )

        context["projects"] = projects

        return context
