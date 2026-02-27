from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock


class ProjectLinkBlock(blocks.StructBlock):
    label = blocks.CharBlock(
        help_text="Visible text, ej: Demo, Code, API",
    )

    url = blocks.URLBlock()

    icon = blocks.CharBlock(
        required=False,
        help_text="Lucide icon name, ej: github, external-link",
    )

    class Meta:
        icon = "link"
        label = "Project Link"


class ProjectContentBlock(blocks.StreamBlock):
    heading = blocks.CharBlock(form_classname="full title")
    paragraph = blocks.RichTextBlock()
    image = ImageChooserBlock()
    quote = blocks.BlockQuoteBlock()
    code = blocks.TextBlock()
