from django.db import models

from wagtail.contrib.settings.models import register_setting, BaseSiteSetting
from wagtail.admin.panels import FieldPanel, PageChooserPanel, InlinePanel
from wagtail.fields import StreamField
from wagtail.models import Orderable

from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel

from .blocks import SocialLinkBlock


@register_setting
class SiteSocialSettings(BaseSiteSetting):
    social_links = StreamField(
        [("social", SocialLinkBlock())],
        use_json_field=True,
        blank=True,
    )

    panels = [
        FieldPanel("social_links"),
    ]


class NavigationLink(Orderable):
    settings = ParentalKey(
        "core.SiteNavigationSettings",
        related_name="navigation_links",
        on_delete=models.CASCADE,
    )

    title = models.CharField(max_length=50)

    page = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="+",
    )

    external_url = models.URLField(blank=True)

    panels = [
        FieldPanel("title"),
        PageChooserPanel("page"),
        FieldPanel("external_url"),
    ]

    def link(self):
        if self.page:
            return self.page.url
        return self.external_url


@register_setting
class SiteNavigationSettings(BaseSiteSetting, ClusterableModel):
    panels = [
        InlinePanel("navigation_links", label="Navigation Links"),
    ]
